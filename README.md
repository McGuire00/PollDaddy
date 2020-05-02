PollDaddy Hack
This is pretty easy to use. Just download the Python script, and customize the variables.


Disclaimer
Use proxies to submit multiple votes.

Example
If you want to rig this poll: https://poll.fm/10111408 for the answer "Zero". The poll_id comes from the url: https://poll.fm/10111408/. The PDI_answer comes from the looking at the source code for the associated checkbox: <input type="radio" name="PDI_answer" id="PDI_answer41930288" value="46414409">.

Thus, you would want the variables to be set to:

poll_id = 9206448
PDI_answer = 41930288
