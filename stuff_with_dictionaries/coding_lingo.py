jagrons = {
    'hardware':'physical components of a computer you can touch',
    'operating system':'programs that allow applications to communicate with hardware',
    'firmware':'software programs that run at lower level',
    'file extension':'determines what application can be used to open/run the file',
    'source code':'file containing human readable code written using the syntax of a programming language',
    'executable':'file that can be run/executed by an application',
    'bug':'term used to describe any unexpected behaviour by a computer program.',
    'compiler':'program that converts source code into machine readable code',
    'linker':'program used as part of the process of compiling code',
    'command':'instruction given to a program to run a task',
    'terminal':'program providing an interface to input commands',
    'debugger':'tool used to figure out where bugs are in a program',
    'integrated development environment':'applications containing tools to assist in developing software',
    'git':'the most popular software version control system',
    'open source':'sources anyone can use/view/modify because the files are in a public location'
}
for word, meaning in jagrons.items():
    print(f"{word.title()}:\n\t{meaning.capitalize()}.\n")
