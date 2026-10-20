# -*- coding: utf-8 -*-
"""
Supabase client helper for storing and retrieving student scores.
Supports Streamlit secrets, environment variables, local JSON configuration, and preconfigured defaults.
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

# Pre-configured default credentials for the user
DEFAULT_URL = "https://gibrwrsnpzdyaqwxpyil.supabase.co"
DEFAULT_KEY = "sb_secret_sxAqm-PXRd-tO0Bo87ZUGw_l_FlfXID"
DEFAULT_TABLE = "student_scores"


def get_supabase_config():
    """
    Retrieve Supabase URL, Key, and Table Name from available sources with preconfigured fallback.
    """
    url = ""
    key = ""
    table = DEFAULT_TABLE

    # 1. From st.secrets if configured
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

    # 2. From Environment variables
    if not url:
        url = os.environ.get("SUPABASE_URL", "")
    if not key:
        key = os.environ.get("SUPABASE_KEY", os.environ.get("SUPABASE_SECRET_KEY", os.environ.get("SUPABASE_ANON_KEY", "")))
    if table == DEFAULT_TABLE:
        table = os.environ.get("SUPABASE_TABLE", DEFAULT_TABLE)

    # 3. From local supabase_config.json
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

    # 4. From st.session_state if saved dynamically in current session
    try:
        if not url and "supabase_url" in st.session_state:
            url = st.session_state["supabase_url"]
        if not key and "supabase_key" in st.session_state:
            key = st.session_state["supabase_key"]
        if "supabase_table" in st.session_state:
            table = st.session_state["supabase_table"]
    except Exception:
        pass

    # 5. Preconfigured defaults (Guarantee zero configuration friction)
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
    Test connection to Supabase and check if table is reachable.
    """
    if not HAS_SUPABASE_LIB:
        return False, "Thư viện supabase chưa được cài đặt."

    cfg = get_supabase_config()
    target_url = url or cfg["url"]
    target_key = key or cfg["key"]
    target_table = table or cfg["table"]

    if not target_url or not target_key:
        return False, "Chưa cung cấp đầy đủ Supabase URL và API Key."

    try:
        client = create_client(target_url, target_key)
        res = client.table(target_table).select("*").limit(1).execute()
        return True, f"Kết nối Supabase và bảng '{target_table}' thành công!"
    except Exception as e:
        err_msg = str(e)
        if "relation" in err_msg and "does not exist" in err_msg or "PGRST205" in err_msg:
            return False, f"Kết nối Supabase thành công, nhưng bảng '{target_table}' chưa được tạo."
        return False, f"Lỗi kết nối: {err_msg}"


def save_score_to_supabase(student_name: str, score_str: str):
    """
    Insert student test record into Supabase:
    Only saves student name and score (câu đúng/50).
    """
    client = get_supabase_client()
    if not client:
        return False, "Chưa cấu hình kết nối Supabase."

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
    Fetch student scores from Supabase ordered by latest first.
    Returns list of dicts suitable for st.dataframe: [Thời gian, Học viên, Điểm].
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
