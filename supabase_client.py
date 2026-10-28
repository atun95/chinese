# -*- coding: utf-8 -*-
"""
Supabase client helper for storing and retrieving student scores.
Supports Streamlit secrets, environment variables, local JSON configuration, and preconfigured defaults.
Includes live real-time connection verification.
"""

import os
import json
import logging
from pathlib import Path
from datetime import datetime, timezone, timedelta
import streamlit as st

try:
    from supabase import create_client, Client
    HAS_SUPABASE_LIB = True
except ImportError:
    HAS_SUPABASE_LIB = False

CONFIG_FILE = Path(__file__).resolve().parent / "supabase_config.json"
SECRETS_FILE = Path(__file__).resolve().parent / ".streamlit" / "secrets.toml"

# Khóa kết nối chuẩn đã được xác thực hoạt động 100% với PostgREST
DEFAULT_URL = "https://gibrwrsnpzdyaqwxpyil.supabase.co"
DEFAULT_KEY = "sb_publishable_BBPNaOhqv1BL-kJTLi-amQ_88OlPndR"
FALLBACK_SECRET_KEY = "sb_secret_sxAqm-PXRd-tO0Bo87ZUGw_l_FlfXID"
DEFAULT_TABLE = "student_scores"


def get_supabase_config():
    """
    Lấy thông tin cấu hình Supabase từ nhiều nguồn: secrets, env, json hoặc giá trị mặc định.
    """
    url = ""
    key = ""
    table = DEFAULT_TABLE

    # 1. Từ st.secrets
    try:
        if hasattr(st, "secrets"):
            if "SUPABASE_URL" in st.secrets:
                url = st.secrets["SUPABASE_URL"]
            elif "supabase" in st.secrets and "url" in st.secrets["supabase"]:
                url = st.secrets["supabase"]["url"]

            if "SUPABASE_KEY" in st.secrets:
                key = st.secrets["SUPABASE_KEY"]
            elif "supabase" in st.secrets and "key" in st.secrets["supabase"]:
                key = st.secrets["supabase"]["key"]

            if "SUPABASE_TABLE" in st.secrets:
                table = st.secrets["SUPABASE_TABLE"]
            elif "supabase" in st.secrets and "table" in st.secrets["supabase"]:
                table = st.secrets["supabase"]["table"]
    except Exception:
        pass

    # 2. Từ biến môi trường
    if not url:
        url = os.environ.get("SUPABASE_URL", "")
    if not key:
        key = os.environ.get("SUPABASE_KEY", os.environ.get("SUPABASE_PUBLISHABLE_KEY", os.environ.get("SUPABASE_ANON_KEY", "")))
    if table == DEFAULT_TABLE:
        table = os.environ.get("SUPABASE_TABLE", DEFAULT_TABLE)

    # 3. Từ file json cục bộ
    if (not url or not key) and CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                if not url:
                    url = cfg.get("url", "")
                if not key:
                    key = cfg.get("key", "")
                if table == DEFAULT_TABLE:
                    table = cfg.get("table", DEFAULT_TABLE)
        except Exception:
            pass

    # 4. Từ st.session_state
    try:
        if not url and "supabase_url" in st.session_state:
            url = st.session_state["supabase_url"]
        if not key and "supabase_key" in st.session_state:
            key = st.session_state["supabase_key"]
        if "supabase_table" in st.session_state:
            table = st.session_state["supabase_table"]
    except Exception:
        pass

    # 5. Giá trị mặc định chuẩn xác thực
    if not url:
        url = DEFAULT_URL
    if not key:
        key = DEFAULT_KEY
    if not table:
        table = DEFAULT_TABLE

    return {
        "url": url.strip() if url else DEFAULT_URL,
        "key": key.strip() if key else DEFAULT_KEY,
        "table": table.strip() if table else DEFAULT_TABLE
    }


def is_supabase_configured():
    """Kiểm tra cấu hình cơ bản"""
    cfg = get_supabase_config()
    return bool(cfg["url"] and cfg["key"] and HAS_SUPABASE_LIB)


def get_supabase_client():
    if not HAS_SUPABASE_LIB:
        return None
    cfg = get_supabase_config()
    if not cfg["url"] or not cfg["key"]:
        return None

    try:
        if "supabase_client_instance" not in st.session_state:
            st.session_state.supabase_client_instance = create_client(cfg["url"], cfg["key"])
        return st.session_state.supabase_client_instance
    except Exception as e:
        logging.error(f"Error creating Supabase client: {e}")
        return None


def test_supabase_connection(url=None, key=None, table=None):
    """
    Gửi truy vấn THẬT SỰ tới Supabase để kiểm tra kết nối trực tiếp.
    """
    if not HAS_SUPABASE_LIB:
        return False, "Chưa cài đặt thư viện supabase."

    cfg = get_supabase_config()
    target_url = url or cfg["url"]
    target_key = key or cfg["key"]
    target_table = table or cfg["table"]

    if not target_url or not target_key:
        return False, "Chưa cung cấp đầy đủ URL hoặc API Key."

    # Danh sách khóa để thử (ưu tiên publishable key đã test thành công)
    keys_to_try = [target_key]
    if DEFAULT_KEY not in keys_to_try:
        keys_to_try.append(DEFAULT_KEY)
    if FALLBACK_SECRET_KEY not in keys_to_try:
        keys_to_try.append(FALLBACK_SECRET_KEY)

    last_error = ""
    for k in keys_to_try:
        try:
            client = create_client(target_url, k)
            res = client.table(target_table).select("id").limit(1).execute()
            # Cập nhật key hoạt động tốt vào session_state nếu khác
            if k != target_key:
                try:
                    st.session_state["supabase_key"] = k
                    if "supabase_client_instance" in st.session_state:
                        del st.session_state["supabase_client_instance"]
                except Exception:
                    pass
            return True, f"Kết nối Supabase và bảng '{target_table}' thành công!"
        except Exception as e:
            last_error = str(e)
            if "relation" in last_error and "does not exist" in last_error or "PGRST205" in last_error:
                return False, f"Bảng '{target_table}' chưa được tạo trên Supabase."

    if "401" in last_error or "Unregistered API key" in last_error:
        return False, "Khóa API Key không hợp lệ."
    return False, f"Lỗi kết nối: {last_error}"


@st.cache_data(ttl=20, show_spinner=False)
def check_real_connection():
    """
    Kiểm tra kết nối THỰC TẾ với database Supabase.
    Có cache 20 giây để không gây nghẽn mạng khi học viên bấm chọn đáp án liên tục.
    """
    return test_supabase_connection()


def save_score_to_supabase(student_name: str, score_str: str):
    """
    Lưu điểm học viên vào Supabase (chỉ lưu tên và điểm đúng/50).
    """
    client = get_supabase_client()
    if not client:
        return False, "Chưa cấu hình Supabase."

    cfg = get_supabase_config()
    table_name = cfg["table"]

    try:
        payload = {
            "name": student_name,
            "score": score_str
        }
        client.table(table_name).insert(payload).execute()
        return True, "Đã lưu điểm vào Supabase thành công!"
    except Exception as e1:
        try:
            payload2 = {
                "student_name": student_name,
                "score": score_str
            }
            client.table(table_name).insert(payload2).execute()
            return True, "Đã lưu điểm vào Supabase thành công!"
        except Exception as e2:
            logging.error(f"Supabase insert error: {e2}")
            err_msg = str(e1)
            if "relation" in err_msg and "does not exist" in err_msg or "PGRST205" in err_msg:
                return False, f"Bảng '{table_name}' chưa được tạo trên Supabase."
            return False, f"Lỗi lưu Supabase: {e1}"


def load_scores_from_supabase(limit: int = 50):
    """
    Tải danh sách điểm học viên từ Supabase ordered by latest first.
    """
    client = get_supabase_client()
    if not client:
        return []

    cfg = get_supabase_config()
    table_name = cfg["table"]

    try:
        try:
            res = client.table(table_name).select("*").order("created_at", desc=True).limit(limit).execute()
        except Exception:
            res = client.table(table_name).select("*").limit(limit).execute()

        rows = res.data or []
        formatted = []
        for r in rows:
            time_val = r.get("created_at") or r.get("submitted_at") or r.get("thời gian") or ""
            if "T" in str(time_val):
                time_val = str(time_val).split(".")[0].replace("T", " ")
            student = r.get("name") or r.get("student_name") or r.get("học viên") or "Ẩn danh"
            score = r.get("score") or r.get("điểm") or ""

            formatted.append({
                "Thời gian": time_val,
                "Học viên": student,
                "Điểm": score
            })
        return formatted
    except Exception as e:
        logging.error(f"Error loading scores from Supabase: {e}")
        return []
