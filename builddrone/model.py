from elixir import metadata, options_defaults, Entity, Field
from elixir import Integer, Unicode, UnicodeText, Numeric
from elixir import setup_all, OneToMany, ManyToOne
import sqlalchemy

metadata.bind = "sqlite:///builddrone.sqlite"
metadata.bind.echo = True #TODO Disable. Debugs all SQL ops
options_defaults['session'] =  sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker(autocommit=True,autoflush=True))

class JobId(Entity):
    arch = Field(UnicodeText)
    gcc = Field(UnicodeText)
    name = Field(UnicodeText, synonym='project')
    uuid = Field(UnicodeText, primary_key=True)
    blob = Field(UnicodeText)
    status = Field(UnicodeText)
    @property
    def jobid(self):
        return self.name +'-'+ self.arch +'-'+ self.gcc +'-'+ self.uuid

class Project(Entity):
    vcs = Field(UnicodeText)
    name = Field(UnicodeText, primary_key=True)
    branches = OneToMany('Branch')
    owner = Field(UnicodeText)
    
class Branch(Entity):
    project = ManyToOne('Project')
    commits = OneToMany('Commit')
class Commit(Branch):
    branch = ManyToOne('Branch')
    sha = Field(UnicodeText, primary_key=True)
    time = Field(Numeric)
    builds = Field(Numeric, default=0)

if __name__ == '__main__':
    setup_all()