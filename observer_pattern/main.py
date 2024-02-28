from subscriber_utils import SubscriberUtils
from subscriber import Subscriber


#declare a object for pup-sub
kafka=SubscriberUtils()

#create two subscribers
s1=Subscriber()
s2=Subscriber()

#add subscriber 1 
kafka.add_subscriber(s1)

#add message to Kafka 
kafka.messages="lol"

#add subscriber 2
kafka.add_subscriber(s2)


#Print messages to check all the subs have same message 
print(kafka.messages)
print(s1.messages)
print(s2.messages)
