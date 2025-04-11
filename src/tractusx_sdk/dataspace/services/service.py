#################################################################################
# Eclipse Tractus-X - Software Development KIT
#
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the
# License for the specific language govern in permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0
#################################################################################

from abc import ABC, abstractmethod


class BaseService(ABC):
    """
    Base service class
    """

    @abstractmethod
    def __init__(self, version: str, base_url: str, headers: dict = None):
        """
        A base init method for services inheriting this class.
        Each service should implement its own init method, with at least the version and base_url parameters.

        :param version: The version of the service
        :param base_url: The base URL of the service
        :param headers: The headers to be used for requests to the service
        """
        pass

    @classmethod
    def builder(cls):
        """
        This method is intended to return a builder for services inheriting this class.
        This means that such a service should implement its own `_Builder` inner class.
        By default, the `Service._Builder` class is used.

        :return: a builder for the model inheriting this class
        """
        return cls._Builder(cls)

    class _Builder:
        """
        Default _Builder class for a Service.
        """

        def __init__(self, cls):
            self.cls = cls
            self._data = {}

        def version(self, version: str):
            self._data["version"] = version
            return self

        def base_url(self, base_url: dict):
            self._data["base_url"] = base_url
            return self

        def headers(self, headers: dict):
            self._data["headers"] = headers
            return self

        def data(self, data: dict):
            """
            This method is intended to set all the data of the adapters inheriting this class.

            It can be used to set all the data of the adapter in a single call, without the need to declare
            each builder method separately. This is useful for cases where an adapter may deviate from its base
            adapter implementation, and the base adapter builder methods are not sufficient to set all the necessary data.
            """

            self._data.update(data)
            return self

        def build(self):
            """
            :return: an instance of the class inheriting the base adapter
            """
            return self.cls(**self._data)