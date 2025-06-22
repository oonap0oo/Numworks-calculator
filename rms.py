from math import *

# info waveforms: name, average, rms
waveforms=(
  ("sine","0","1/sqrt(2)*A"),
  ("half wave sine","1/pi*A","1/2*A"),
  ("full wave sine","2/pi*A","1/sqrt(2)*A"),
  ("sawtooth","1/2*A","1/sqrt(3)*A"),
  ("pulse","duty_cycle*A","sqrt(duty_cycle)*A")
  )

# choose a waveform
def list_waveforms():
  print("\navg and rms of waveforms")
  print("------------------------")
  loop=True
  while loop:
    for n,wf in enumerate(waveforms):
      s="{0}: {1}".format(n,wf[0])
      print(s)
    answer=input("Choose the waveform number: ")
    try:
      choice=int(answer)
    except:
      print("Choise must be number")
    else:
      choice=int(answer)
      if len(waveforms)>choice>-1:
        loop=False
  return waveforms[choice]

# display characteristics and input values
def display_waveform(wf):
  loop=True
  while loop:
    print("\nWaveform: "+wf[0])
    print("Amplitude: A")
    print("Average value = {0}".format(wf[1]))
    print("RMS value = {0}".format(wf[2]))
    answer=input("Enter amplitude value A: ")
    try:
      A=float(answer)
    except:
      print("invalid amplitude {0}".format(answer))
    else:
      loop=False
  return A

# in case pulse input duty cycle
def get_dutycycle():
  loop=True
  while loop:
    answer=input("Enter duty cycle\nbetween 0 and 1.0: ")
    try:
      d_cycle=float(answer)
    except:
      print("invalid duty cycle {0}".format(answer))
    else:
      if 0<=d_cycle<=1:
        loop=False
      else:
        print("Duty cycle must be between 0 and 1.0")
  return d_cycle

# calc and show avg and rms
def calc_avg_rms(wf,A,duty_cycle=1):
  print("\n{0}\nwith amplitude {1}".format(wf[0],A))
  avg=float(eval(wf[1]))
  print("Average value={0:.8}".format(avg))
  rms=float(eval(wf[2]))
  print("RMS value={0:.8}".format(rms))
    
loop=True
while loop:
  wf=list_waveforms()
  A=display_waveform(wf)
  if wf[0]=="pulse":
    duty_cycle=get_dutycycle()
    calc_avg_rms(wf,A,duty_cycle)
  else:
    calc_avg_rms(wf,A)
  answer=input("Continue? y/n ")
  if answer.lower()!="y":
    loop=False
