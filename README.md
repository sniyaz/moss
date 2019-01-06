# MOSS #

These are the files used to run MOSS in CSE 373 in AU18. This is intended to be 
a guide for using MOSS that future 373 TAs can make use of.

If you have any questions, please email me at sniyaz@cs.washington.edu.

### Step 1: Downloading Student Submissions ###

First, you'll need to download all student submissions into a directory. Each 
submission should be a unique folder, and all of these submission folders should
have identical structure. In AU18 we had a script to do this from GitLab 
(please see `clone-repos.sh`). Let's call this directory (containing a 
subdirectory corresponding to each student submission `hwX_submissions`.

**Note**: You should include in `hwX_submissions` the project skeleton as well,
in addition to any solutions pulled from GitHub (students like to copy from 
these, so it's usually a good idea to do a quick prowl.)

Also create two other directories on the same level as `hwX_submissions`, and 
call them `hwX_prune` and `hwX_join`. These should be empty for now, but we'll
fill them in later.

### Step 2: Preprocessing Submissions

The next thing we need to do is to extract the edited student files that we actually need to run MOSS on. We could just send the entire submission directories to the MOSS server, but that would be slow and make the plagiarism check less effective.

If you look in `prune_files.py`, you should see some lists of strings with the name `EDIT_FILES`, most of them commented out. These are hardcoded lists of which skeleton files within the project directory were edited by students. These are the files used by AU18, so you may have to tweak these for your assignment.

Once you do though, you can extract the files that students actually edited by doing this:

`python3 prune_files.py hwX_submissions/ hwX_prune/ hwX_join/`

Where the three `hwX_*` directories were set up according to the previous section. Remember that `hwX_submissions/` should contain a subdirectory for the skeleton code before you do this, for example `hwX_submissions/hwX_skel/`.

This script outputs in `hwX_prune/` and `hwX_join/`. You won't directly use the contents of `hwX_prune/`, which contains each submission directory in `hwX_submissions/`, but strips out all files not edited by students. You *will* use `hwX_join/`, which takes each pruned submission directory in `hwX_prune/` and smashes its files into a single large file. Thus, this directory contains one file per submission with all the code edited by that specific student.

### Step 3: Run MOSS

Almost there! First, `mv` the joined skeleton code file (i.e. `hwX_skel_join.java`) out of `hwX_join/` and to the same level as the three `hwX_*` directories. Now, send the joined skeleton and all of the joined student submissions to the MOSS server:

`chmod ug+x moss.pl`

This just makes the MOSS Pearl script executable. You only need to do this once.

`./moss.pl -l java -b hwX_skel_join.java hw2_join/*.java`

<!--**Note:** Everything so far assumes Java as the language since most data structures course are taught in it. If you're using a different language, you'll just need to supply the appropriate argument after -l.-->

This actually sends code to the MOSS servers. By using the `-b` argument, we're telling MOSS to use the joined skeleton as a base file to improve accuracy.

At this point, you may need to wait a while. I've observed strange issues on certain networks that can cause MOSS to just time out or die. I've always gotten things to work on CSE's `tricycle` servers, so give those a try here if you run into this issue (ask a grad student TA for help if you don't have access).

Assuming everything went well, MOSS should spit back a URL with the results. Give those a look. Make sure not to post this URL publicly (only post on your staff Slack, etc) since anybody (!) with this URL can see the MOSS results. This is security through obscurity, plain and simple.

### Step 4: Parse Results

Here's a quick guide to parsing the results. The highest matches will be near the top of the list, with an accompanying percentage. A high percentage does *not* mean the student necessarily cheated. In every case a human **must** go through and verify misconduct. 

When you click on a certain match, MOSS will have different sections of the code highlighted with different colors. If you click on two areas with the same color, you can compare regions of both submissions that MOSS has flagged as similar.

### Step 5: Meet with Students

This is probably the least fun part of the entire process, but the most important by far. If MOSS finds something strange, students have a right to explain themselves. Make sure to email students explaining why they need to meet with you. Here's a template you can start with that we used in AU18:

https://docs.google.com/document/d/1o_EqKy0wwfL9apdJLFpBZoMc6yOwIB6qjeAlZlwc_Xw/edit?usp=sharing

Generally, it's better to run MOSS and send these emails as early as possible. Don't chase down cases towards the end of the quarter. Trust me, it's extremely stressful and not worth it. MOSS early and MOSS often.

Once you do meet with students, show them the evidence against them and explain why you suspect plagiarism. If this was a team project, it's important to have *all* team members present to make sure they're on the same page (we had an issue with this in AU18). Also give the students a chance to explain themselves, and  try not to make them feel as if they're on trial.

After this meeting, you need to decide whether to punish a student, either by docking points for a light offense or zeroing out the entire HW for an egregious one. Remember that at UW, a student has to **explicitly** agree to a punishment to have it applied. Make sure to get this consent from all punished students **in writing** (i.e. an email) to make sure you've covered your ass.

If you decide to punish a student and they do not consent to it, you'll need to escalate things to the university. We never actually had to do this, but Pim Lustig and Dan Grossman are good people to know should you find yourself in this situation.