# fake_unity.py

import zmq
import time

def main():
    ip = "172.24.71.240"  # Minerva's IP
    port_keypoints = 8087
    port_button = 8089
    port_pause = 8091

    context = zmq.Context()

    # --- Socket for keypoints ---
    socket_keypoints = context.socket(zmq.PUSH)
    socket_keypoints.connect(f"tcp://{ip}:{port_keypoints}")

    # --- Socket for button feedback (resolution) ---
    socket_button = context.socket(zmq.PUSH)
    socket_button.connect(f"tcp://{ip}:{port_button}")

    # --- Socket for pause status ---
    socket_pause = context.socket(zmq.PUSH)
    socket_pause.connect(f"tcp://{ip}:{port_pause}")

    keypoint_data = (
        b'relative:0,0,0|0,0,0|-0.010497,-0.011554,0.020069|-0.02802849,-0.01915771,0.03595842|-0.02802848,-0.0191577,0.06847131|-0.02802847,-0.01915769,0.1022644|-0.02355066,-0.007316453,0.09599622|-0.02355065,-0.007316454,0.1339235|-0.02355065,-0.007316453,0.1582271|-0.00172589,-0.002543154,0.0956466|-0.00172589,-0.002543155,0.1385736|-0.00172589,-0.002543156,0.1661231|0.01746524,-0.006529306,0.08869377|0.01746526,-0.006529307,0.1276898|0.01746526,-0.006529308,0.1542632|0.02299857,-0.009419831,0.03407355|0.02299638,-0.009420833,0.07972407|0.02299638,-0.009420832,0.1104445|0.02299638,-0.009420834,0.1307558|-0.02905545,-0.01848733,0.1268551|-0.02325503,-0.00629138,0.1805905|-0.00141722,-0.001405853,0.191088|0.01772316,-0.004921136,0.1785893|0.02274989,-0.008204747,0.1526781:' )

    try:
        while True:
            # 1. Send keypoints
            socket_keypoints.send(keypoint_data)
            print("📤 Sent keypoints.")

            # 2. Send resolution button ("High" or "Low")
            socket_button.send(b'Low')  # or b'Low'
            print("📤 Sent resolution: Low")

            # 3. Send pause status ("High" or "Low")
            socket_pause.send(b'High')  # or b'Low'
            print("📤 Sent pause: High")

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("🛑 Stopped.")

if __name__ == "__main__":
    main()
