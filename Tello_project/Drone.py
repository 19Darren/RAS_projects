from Class_Drone import *

ArUcoSize = 65     # ArUco marker size in mm

if __name__ == '__main__':
    print("init")

    Dron = ClassDron(Controller = StateMachine(), ArUcoSize = ArUcoSize)
    Dron.start()
    time.sleep(1)
    print("ready")
    Dron.video()
    Dron.send("takeoff")

    Prep(Dron)
    Dron.AutonomicFlightEnable()
    time.sleep(20)
    Dron.AutonomicFlightDisable()
    Dron.stop_video()