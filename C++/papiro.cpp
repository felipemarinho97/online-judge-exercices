#include <ncurses.h>
#include <string>
#include "Editor.h"

using namespace std;

void init_curses() {
	initscr();
	noecho();
	cbreak();
	keypad(stdscr, true);
}

int main(int argc, char* argv[]) {
	Editor ed;
	string filename = "";
	if (argc > 1) {
		filename = argv[1];
		ed = Editor(filename);
	}
	else {
		ed = Editor();
	}
	init_curses();
	while(ed.getMode() != 'x')
	{
	    ed.updateStatus();
	    ed.printStatusLine();
	    ed.printBuff();
	    int input = getch();                // Blocking until input
	    ed.handleInput(input);
	}
	refresh();
	endwin();
	return 0;

}
