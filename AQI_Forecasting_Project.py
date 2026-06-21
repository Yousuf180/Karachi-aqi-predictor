# ============================================
# START STREAMLIT WITH PUBLIC URL
# ============================================

import subprocess
import time
from pyngrok import ngrok
import os

print("🚀 Starting Streamlit server...")

# Kill any existing Streamlit processes
import signal
try:
    subprocess.run(['pkill', '-f', 'streamlit'], check=False)
    time.sleep(2)
except:
    pass

# Start Streamlit in background
streamlit_process = subprocess.Popen(
    ['streamlit', 'run', 'app.py', '--server.port', '8501', '--server.headless', 'true'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Wait for Streamlit to start
print("⏳ Waiting for Streamlit to start...")
time.sleep(5)

# Create ngrok tunnel
print("🔗 Creating public URL...")
try:
    # Terminate any existing ngrok tunnels
    ngrok.kill()

    # Create new tunnel
    public_url = ngrok.connect(8501)
    print("\n" + "="*60)
    print("✅ STREAMLIT APP IS LIVE!")
    print("="*60)
    print(f"🔗 Public URL: {public_url}")
    print(f"📱 Open this URL in your browser")
    print("="*60)
    print("\n⚠️ Keep this cell running - do not stop it!")
    print("💡 To stop: Click the stop button (⏹️) or restart runtime")

except Exception as e:
    print(f"❌ Error creating tunnel: {e}")
    print("\nTrying alternative method...")

    # Alternative: use localhost.run
    try:
        !streamlit run app.py --server.port 8501 &
        time.sleep(5)
        !npx localtunnel --port 8501
    except:
        print("Please run: !streamlit run app.py")
