    from flask import Flask, request
    import re
    app = Flask(__name__)

    @app.route("/", methods=["GET","POST"])
    def home():
        t=""
        if request.method=="POST":
            m=re.search(r'eat=([^&]+)', request.form.get("link",""))
            t=f"<p style='color:#00ff00'>✅ TOKEN: {m.group(1)}</p>" if m else "<p style='color:red'>❌ No se encontró eat=</p>"
        return f"""<!DOCTYPE html><html><head><title>DARK FF V1</title><meta name=viewport content=width=device-width,initial-scale=1><style>body{{background:#0a0a0a;color:#fff;text-align:center;padding:20px;font-family:Arial}}h1{{color:#ff6b00}}.btn{{background:red;color:#fff;padding:12px;border-radius:8px;text-decoration:none}}input{{width:80%;padding:12px;background:#111;color:#fff;border:1px solid #333;border-radius:8px}}button{{width:80%;padding:14px;background:orange;color:#fff;border:none;border-radius:8px;margin-top:10px}}</style></head><body><h1>⚡ DARK FF V1 BIO ⚡</h1><a href=https://ticket.kiosgamer.co.id class=btn target=_blank>1. IR A KIOSGAMER</a><form method=post><p>Pega el link con eat=</p><input name=link placeholder="Pega aqui..." required><button>2. EXTRAER TOKEN</button></form>{t}</body></html>"""
