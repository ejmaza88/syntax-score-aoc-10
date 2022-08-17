### Advent of Code Day 10 Challenge
Completed AoC Day 10 challenge as part of the take home exersice
***

### Python Requirements
python 3.8+
***

### Run 
run script:

``python main.py``

run test:

``python test_main.py``
***

### Final Thoughts
My initial approach was to tackle both parts independent of each other.
Then realized that part of the code overlaps when finding the solution 
for each part. This is more prominent when looking at functions 
`syntax_scoring_part_one()` and `syntax_scoring_part_one()` where the body
of each is reading the file once again. Something to consider is to refactor
the logic that is shared between both parts to avoid having to open the file 
twice. This is one of many approaches, although it satisfies requirements, there
is room for improvement. Due to time constraints I didn't fully engaged on some
of the improvements I have in mind, didn't want to jeopardize anything that 
would've had prevented me from completing this on time. 

#### ToDo:
My main focus was to complete both parts of the challenge, due to it, the majority
of the time went to understanding the requirements not much time was allocated to
code cleanup. My hope is to add more comments and docstrings to make it easy to the
reader understand the logic.