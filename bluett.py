from bluepy import btle

print "Connecting...."
dev = btle.Peripheral("B8:27:EB:54:0D:12")

print "Services...."
for svc in dev.services:
    print str(svc)
