from elixir import metadata, using_options, Entity, Field
from elixir import Integer, Unicode, UnicodeText, Numeric

metadata.bind = "sqlite:///builddrone.sqlite"
metadata.bind.echo = True #TODO Disable.

class JobId(Entity):
    arch = Field(UnicodeText)
    gcc = Field(UnicodeText)
    name = Field(UnicodeText, synonym='project')
    uuid = Field(UnicodeText, primary_key=True)
    blob = Field(UnicodeText)
    status = Field(UnicodeText)

class Project(Entity):
    vcs = Field(UnicodeText)
    name = Field(UnicodeText, primary_key=True)

class Commit(Entity):
    project = Field(UnicodeText)
    branch = Field(UnicodeText)
    sha = Field(UnicodeText, primary_key=True)
    time = Field(Numeric)
    builds = Field(Numeric, default=0)
    