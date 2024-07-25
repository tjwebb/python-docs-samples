# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re

import adaptation_v2_inline_phrase_set
from google.api_core.retry import Retry

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")


@Retry()
def test_adaptation_v2_inline_phrase_set() -> None:

    response = adaptation_v2_inline_phrase_set.adaptation_v2_inline_phrase_set()

    assert re.search(
        r"the word is fare",
        response.results[0].alternatives[0].transcript,
        re.DOTALL | re.I,
    )
