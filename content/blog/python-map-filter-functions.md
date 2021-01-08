---
title: "Python: Map and Filter functions"
date: 2021-01-02 # YYYY-MM-DD
featureImage: images/allpost/python-post.png
postImage: images/single-blog/Python Wallpaper.jpg
---


Well, it's my first blog post I'm writing myself. And I would immediately like to say why I decided to blog at all.

Let me give you an example. Imagine that you need to find any information on the Internet, library sources, etc. Often, you don't limit yourself to just one source of information because you need to make sure that it is totally true and to look at the issue from different points of view. And, of course, you may be taking notes.

The idea behind this blog for me is to take notes of the information that I find on the Internet while studying, completing projects, and so on. This is information that I find quite useful and that may be useful in the future.

And I hope that it will be useful to others as well.

Well, let's get started ...

## map() function

The python's ```map``` function is used in order to apply any function you need to all the items in iterator (list, dict, e.t.c.) you put into the map function. It returns iterator object. But you can transfer it to the list() or other type of sequence.

It has the following syntax:
``` py
map(function, iterable, [iterable_2, iterable_3, ...])
```
or 
``` py
map(lambda item: item[] expression, iterable)
```
(if lambda-function is used)

For example, let's imagine next program:

We have 2 lists of numbers.
``` py
a = [1,2,3,4,5]
b = [3,15,10,20,1]
```


And we want to sum these lists by multiplying each element of the first list by two and dividing each element of the second list by two.

``` py
summed_numbers = list(map(lambda x,y:x*2 + y/2, a, b))
print(summed_numbers)
```

``` py
--- OUTPUT ---
[3.5, 11.5, 11.0, 18.0, 10.5]
```

## filter() function
The python's ```filter()``` function takes a lambda function together with a list as the arguments. It has the following syntax:

``` py
filter(object, iterable)
```

The ```object``` here should be a lambda function which returns a boolean value. The object will be called for every item in the ```iterable``` to do the evaluation. The result is either a True or a False for every item. Note that the function can only take one iterable as the input.

A lambda-function, along with the list to be evaluated, is passed to the filter() function. The filter() function returns a list of those elements that return True when evaluated by the lambda funtion. Consider the example given below:

``` py
# The list of numbers is given
numbers_list = [2, -6, 18, 11, 4, 12, -7, 13, 17]

# We will leave only those numbers that are greater than 7
filtered_list = list(filter(lambda num: (num > 7), numbers_list))

print(filtered_list)
```

The result of the program is:

``` py
---OUTPUT---
[18, 11, 12, 13, 17]
```

Based on the overview of such simple programs using the `` map() `` and ```filter()``` functions, it is clear now that these functions can be really useful in some cases when you need to filter something or apply any operation to the iterator.