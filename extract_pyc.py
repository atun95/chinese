import marshal
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pyc_path = r"lessons\__pycache__\lessons_data.cpython-313.pyc"

try:
    with open(pyc_path, "rb") as f:
        header = f.read(16)
        code_obj = marshal.load(f)
        
    print("Successfully loaded code object!")
    
    # Dump string constants and tuples in range 1200 to 1292
    for idx in range(1200, 1292):
        c = code_obj.co_consts[idx]
        if isinstance(c, str):
            print(f"Constant {idx}: {repr(c)}")
        elif isinstance(c, (tuple, list)):
            print(f"Constant {idx} ({type(c).__name__}): {c}")
                
except Exception as e:
    import traceback
    traceback.print_exc(file=sys.stdout)
    sys.exit(1)
