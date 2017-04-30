from restless.fl import FlaskResource
from restless.preparers import FieldsPreparer

from ..models import User

class UserResource(FlaskResource):
    preparer = FieldsPreparer(
        fields = {
            'uid': 'uid',
            'username': 'username',
            'passhash': 'passhash',
        }
    )

    def is_authenticated(self):
        # Open everything wide!
        # DANGEROUS, DO NOT DO IN PRODUCTION.
        return True

    # GET /api/users/
    def list(self):
        return User.nodes.all()

    # GET /api/users/<pk>/
    def detail(self, pk):
        return User.nodes.get(uid=pk)

    # POST /api/users/
    def create(self):
        user = User(
            # uid=self.data['uid'],
            username=self.data['username'],
            password=self.data['password'],
        ).save()
        return user

    # PUT /api/users/<pk>/
    def update(self, pk):
        try:
            user = User.nodes.get(uid=pk)
        except User.DoesNotExist:
            user = User()

        if self.data['username']:
            user.username = self.data['username']
        if self.data['password']:
            user.hash_password(self.data['password'])
        user.uid = pk
        user.save()
        return user

    # DELETE /api/users/<pk>/
    def delete(self, pk):
        User.nodes.get(uid=pk).delete()
