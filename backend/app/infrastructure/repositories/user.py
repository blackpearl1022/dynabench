# Copyright (c) MLCommons and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from app.infrastructure.models.models import User
from app.infrastructure.repositories.abstract import AbstractRepository


class UserRepository(AbstractRepository):
    def __init__(self) -> None:
        super().__init__(User)
