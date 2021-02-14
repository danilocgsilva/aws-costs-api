# Classes in the current folder:

## Class AWSCosts

What you will use to fetch costs from your AWS account.

You have two methods here:

* `getCosts`: returns the dict with cost data.
* `setProfile`: if you don't have a default profile setted in your environment, or have several profiles, you must specify a profile name before getting information from costs using this method.

## Class DateUtil

This class may not be used directly for some task over cost. But this class is required by main AWSCosts class to performa some data operations:


* `get_date_string_format_from_datetime`: Builds a string format required for a filter required in aws client to fetch costs data.
* `get_month_before`: returns a datetime with a month subtracted, so can be used when fetch costs data.
