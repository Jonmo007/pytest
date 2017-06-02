from pubsub import pub
def listener1(arg1,arg2 = None):
	print('function listener1 received:')
	print(' arg1 = ',arg1)
	print(' arg2 = ',arg2)


def listener2(arg1,arg2 = None):
	print('2 function listener1 received:')
	print('2 arg1 = ',arg1)
	print('2 arg2 = ',arg2)

pub.subscribe(listener1,'rootTopic')
pub.subscribe(listener2,'rootTopic')

obj = dict(a = 456,b = 'abc')
print(obj)
pub.sendMessage('rootTopic',arg1 = 123,arg2 = obj)
pub.sendMessage('rootTopic',arg1 = 456,arg2 = [1,2,3])

