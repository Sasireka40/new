class TireService:
    def __init__(self, pressure_threshold, tread_depth_threshold, rotation_interval):
        self.pressure_threshold = pressure_threshold
        self.tread_depth_threshold = tread_depth_threshold
        self.rotation_interval = rotation_interval

    def is_tire_servicing_needed(self, pressure, tread_depth, mileage):
        if pressure < self.pressure_threshold:
            return True

        if tread_depth < self.tread_depth_threshold:
            return True

        if mileage % self.rotation_interval == 0:
            return True

        return False

# Example usage:
if __name__ == "__main__":
    tire_service = TireService(pressure_threshold=30, tread_depth_threshold=3, rotation_interval=8000)
    pressure_input = float(input("Enter the current tire pressure (PSI): "))
    tread_depth_input = float(input("Enter the current tire tread depth (millimeters): "))
    mileage_input = int(input("Enter the vehicle's current mileage (kilometers): "))
    servicing_needed = tire_service.is_tire_servicing_needed(pressure_input, tread_depth_input, mileage_input)
    if servicing_needed:
        print("Tire servicing is needed.")
    else:
        print("Tire servicing is not needed at the moment.")
