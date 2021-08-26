obj-m += hostname.o
all:
	make -C /lib/$(shell uname -r)/ M=$(shell pwd) 
modulesclean:
	make -C /lib/$(shell uname -r)/ M=$(shell pwd) clean