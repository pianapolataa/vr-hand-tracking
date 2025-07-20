# zmq_pull_test.py

import zmq
import pickle

def main():
    ip = "172.24.71.240"  # Minerva's IP (can also use 0.0.0.0 for bind)
    port = 8087            # The port Unity is PUSHing to

    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind(f"tcp://{ip}:{port}")  # Or just use "0.0.0.0" to accept from any IP

    print(f"🟢 Listening for PUSH data on tcp://{ip}:{port} ...")

    while True:
        try:
            raw = socket.recv()
            print("📥 Raw data received (first 100 bytes):", raw)
        except KeyboardInterrupt:
            print("🛑 Interrupted by user.")
            break

if __name__ == "__main__":
    main()

