#####################################################
# coding=utf-8
# Copyright 2019 Anne Lauscher, Nikolai Rozanov, Olga Majewska, Leonardo Ribeiro, Goran Glavas
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
####################################################

from setuptools import setup, find_packages

setup(
    #
    # SETUP
    #
      name          ='retrograph',
      version       ='0.0.0.1',

      description   ='Retrograph',
      url           ='https://github.com/ai-nikolai/Retrograph',
      author        ='Anne Lauscher, Nikolai Rozanov',
      author_email  ='nikolai@wluper.com',
      license       ='Apache 2.0',
    #
    # Actual packages, data and scripts
    #
      packages      = find_packages(),

      scripts       =[],
    #
    # Requirements
    #
      install_requires=[],
      )
