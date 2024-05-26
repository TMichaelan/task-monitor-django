# pylint: disable=line-too-long, too-many-lines

from unittest.mock import patch, mock_open
import pytest


@pytest.fixture(name="mock_task_data")
def fixture_mock_task_data():
    task_data = """id,status,outcome,fake_outcome_reason,photos_to_resubmit,answer_time,date_created,due_date,date_closed
123,open,,,,1440,1716366616,1716453016,
124,open,,,,1440,1716366391,1716452791,
125,scheduled,authentic,,,1440,1716366070,1716452470,
126,scheduled,fake,inside-label,,120,1716365924,1716373124,
127,in-progress,,,,1440,1716364627,1716451027,
128,update-needed,,,"hardware-engravings, inside-label, serial-number, made-in-label",120,1716362134,1716369334,
129,in-progress,,,,1440,1716361811,1716448211,
130,in-progress,,,,1440,1716361703,1716448103,
131,update-needed,,,"brand-logo, inside-label, zipper-head-front, zipper-head-back, qr-code-label",1440,1716358285,1716444685,
132,in-progress,,,,1440,1716358182,1716444582,
133,in-progress,,,,1440,1716356581,1716442981,
134,scheduled,authentic,,,720,1716356249,1716399449,
135,scheduled,fake,serial-number,,720,1716356230,1716399430,
136,update-needed,,,authenticity-card,120,1716355649,1716362849,
137,closed,authentic,,,30,1716345233,1716347033,1716346679
138,closed,fake,brand-logo,,30,1716345042,1716346842,1716346589
139,closed,UTV,unknown,,1440,1716343850,1716430250,1716356383
"""
    with patch("builtins.open", mock_open(read_data=task_data)) as mock_file:
        yield mock_file
