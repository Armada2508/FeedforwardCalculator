print("Enter the encoder velocity")
velocity = input()
velocity = int(velocity)

print("Enter the maximum output of the motor(default 1023 for Talon SRX and FX feedforward)")
maxPower = input()

if(maxPower == ""):
	maxPower = 1023
else:
	maxPower = int(maxPower)

print("Enter the power commanded to the motor(0.0-1.0)")
power = input()

if(power == ""):
	power = 1.0
else:
	maxPower = int(maxPower)

print("Max Velocity: " + str(velocity / power))
print("Feedforward Gain: " + str(( power * maxPower ) / velocity))