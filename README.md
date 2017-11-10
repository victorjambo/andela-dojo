[![Build Status](https://travis-ci.org/victorjambo/andela-dojo.svg?branch=master)](https://travis-ci.org/victorjambo/andela-dojo)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/victorjambo/andela-dojo/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/victorjambo/andela-dojo/?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/59f0c8cadda84fbd803778823074963a)](https://www.codacy.com/app/victorjambo/andela-dojo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=victorjambo/andela-dojo&amp;utm_campaign=Badge_Grade)
[![Code Coverage](https://scrutinizer-ci.com/g/victorjambo/andela-dojo/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/victorjambo/andela-dojo/?branch=master)
# Dojo
Welcome to Dojo. Dojo is a room allocation app. It enables a user to manage the living and office spaces by allocating the fellows and staff members respectively.


### Dojo requirements

1. An office can occupy a maximum of 6 people.
2. A living space can inhabit a maximum of 4 people.
3. A person to be allocated could be a fellow or staff.
4. Staff cannot be allocated living spaces.
5. Fellows have a choice to choose a living space or not.

## Installation

To set up dojo, make sure that you have python and pip installed.

Use [virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) for an isolated working environment.

Clone the Repo into a folder of your choice
```
git clone https://github.com/victorjambo/andela-dojo.git
```

Create a virtual enviroment.
```
virtualenv venv
```

Navigate to the root folder.
```
cd andela-dojo
```

Install the packages.
```
pip install -r requirements.txt
```

Confirm your installed packages
```bash
$ pip freeze
```

## Usage

To get the app running...

```bash
$ python app.py
```

**1. Create Rooms**

To create a living space or office space, follow the following docopt pattern
```bash
Usage: create_room <room_type> <room_name> ...
```

Creating living spaces
```bash
create_room livingspace red yellow
```

Creating office spaces
```bash
create_room office blue green
```

**2. Add Person**

You can either add a staff member or a fellow with the `add_person` command.
A fellow can either opt in or out of the dojo accomodation plan.
The docopt patter is as follows
```bash
Usage: add_person <first_name> <last_name> <designation> [-w]
```

Add a staff member
```bash
add_person Victor Mutai staff
```

Add a fellow that opts in to the andela accommodation
```bash
add_person Mutai Victor -w
```

Add a fellow that opts out of the andela accommodation
```bash
add_person Mutai Vic fellow
```

**3. Print out data**

The print methods allow you to print out room allocations for all rooms, one room or list of unallocated people.
You can also specify an optional `--o` parameter to write the data to a file.

**Print room**

Print out a list of all people (staff members and fellows) in the specified room

```bash
print_room <room_name>
```

**Print room allocations**

Print out a list of all room allocations at dojo
```bash
print_allocations [--o=filename]
```

**Print unallocated**
Prints out list of all people not allocated a room
```bash
print_unallocated [--o=filename]
```


**4. Quit Dojo!**
To exit from the application, simply type `q` on your app
```bash
q
```

You can get out of the Virtual environment by simply typing `deactivate` on your commandline

## Contributing

Contributions are **welcome** and will be fully **credited**.

We accept contributions via Pull Requests on [Github](https://github.com/victorjambo/andela-dojo).

## Security

If you discover any security related issues, please create an issue.

## Credits

[Victor Mutai](https://github.com/victorjambo)

## License

### The MIT License (MIT)

Copyright (c) 2016 Victor Mutai <victorjambo@live.com>

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.

[ico-license]: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square
