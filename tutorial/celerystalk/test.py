import simpleslicer
from tasks import add
from tasks import enqueue_job


for i in range(10):
	output = 'testing%d.gcode' % i
	print enqueue_job.delay('oshw.stl', 'random.ini', output)
