# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

`ls` = lists all files in the current working directory --> `pwd` useful command to print working directory
   options:
   -a = lists all files including hidden files
   -l = lists files in long format, includes other details about files
   -t = lists files in order of time last modified

`cd` = change directory, `cd ..` =  up one level

`mkdir` = make directory, `touch` = create new empty file

`cp` = copy, syntax: cp [file1] [file 2] [end directory]

`mv` = move command used like cp

`rm` = permanent delete command, can be used with option -r to delete all child directories including specified one.

`echo` = prints the output of the standard input

`cat` = concatenate, general command for read, write, append. syntax cat [option] [end file]
   `>` redirects the output of the cat command into another file and overwrites it.
   `>>` appends the output of the cat command to another file. no overwrite.
   `|` sends (or pipe) operator: sneds the command into another command for further processing.

`grep` =  searches a file for a specified term, can be used with -i option to remove case-sensitivity

`sort [yourtext.txt] | uniq` = uniq command removes all adjacent duplicate entries in a file. piping sort before using uniq is an effective way to remove all duplicates in a file as sort will put all originally non-adjacent entries together in alphabetical order. 

`env` = command to display all environmental variables

`~/.bash_profile` = the bash profile is the file which store the default settings of the command line.
  `alias` = when used inside the command line, assigns an alias to a known command. similar to variables in python
  `export` = exports a defined variable reassignment globally when used in the bash profile.
  `source ~/.bash_profile` = applies the changes made in the bash profile to the command line without restarting.
---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls` = lists all the non-hidden files in the current working directory
`ls -a` = lists all files including hidden files in the current working directory
`ls -l` = lists all files in long format, includes editing permissions
`ls -lh` = lists all files in long format including readable files size (in KB/MB)
`ls -lah` = similar to -lh but includes hidden files
`ls -t` = lists all files in order of time/date last modified
`ls -Glp` = lists files in long format excluding the user name but indicates file type. (highlights subdirectories)

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`-R` = displays all subdirectories and their contents
`-r` = displays the list in reverse order, applies when used in combination with other option
`-p` = marks folders with a /
`-o` = excludes group name
`-1` = displays the list with one entry on one line.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs takes the standard input and converts each line into separate arguments which are read and executed by any following commands. xargs prioritises any initial arguments with these commands over the ones from the standard input. xargs also ignores blank lines.
 
`ls | grep Documents | xargs touch`
