# https://speakerdeck.com/kaityo256/how-to-use-gnu-make
CXX=g++
all: a.out

a.out: main.o sub.o
	$(CXX) main.o sub.o # コマンドの先頭はtab

%.o: %.cpp
	$(CXX) -c $<

clean:
	rm -f a.out *.o

# g++ -MM *.cpp > makefile.dep
-include makefile.dep
