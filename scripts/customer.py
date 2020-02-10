"""
	Formatting Customer Names
"""

def format_customer(fn, ln, location=None):
    full_name = '%s %s' % (fn, ln)
    if location:
        return '%s %s' %(full_name, location)
    else:
        return full_name

