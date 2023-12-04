from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import ForeignKey, Identity, Table, Column, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app import db

class SystemComponent(db.Model, SerializerMixin):
    __tablename__ = "system_components"
    serialize_only = ('id', 'name')
    id: Mapped[int] = mapped_column(Identity(always=True, start=1, increment=1), primary_key=True)
    name: Mapped[str]
    system_changes = relationship("SystemChange", back_populates="component")


class ProjectComponent(db.Model, SerializerMixin):
    __tablename__ = "project_components"
    serialize_only = ('id', 'name')
    id: Mapped[int] = mapped_column(Identity(always=True, start=1, increment=1), primary_key=True)
    name: Mapped[str]
    project_changes = relationship("ProjectChange", back_populates="component")


class Action(db.Model, SerializerMixin):
    __tablename__ = "actions"
    serialize_only = ('id', 'name')
    id: Mapped[int] = mapped_column(Identity(always=True, start=1, increment=1), primary_key=True)
    name: Mapped[str]
    system_changes = relationship("SystemChange", back_populates="action")
    project_changes = relationship("ProjectChange", back_populates="action")


class SystemChange(db.Model, SerializerMixin):
    __tablename__ = "system_changes"
    serialize_rules = ("-id_action", "-id_component")
    id: Mapped[str] = mapped_column(primary_key=True)
    id_action: Mapped[int] = mapped_column(ForeignKey("actions.id"))
    id_component: Mapped[int] = mapped_column(ForeignKey("system_components.id"))
    id_user: Mapped[str]  # = mapped_column(ForeignKey("users.id"))
    new_value: Mapped[str]
    old_value: Mapped[str]
    date: Mapped[str] = mapped_column(TIMESTAMP)
    action: Mapped["Action"] = relationship("Action", back_populates="system_changes")
    component: Mapped["SystemComponent"] = relationship("SystemComponent", back_populates="system_changes")


class ProjectChange(db.Model, SerializerMixin):
    __tablename__ = "project_changes"
    serialize_rules = ("-id_action", "-id_component")
    id: Mapped[int] = mapped_column(primary_key=True)
    id_action: Mapped[int] = mapped_column(ForeignKey("actions.id"))
    id_component: Mapped[int] = mapped_column(ForeignKey("project_components.id"))
    id_user: Mapped[str]  # = mapped_column(ForeignKey("users.id"))
    new_value: Mapped[str]
    old_value: Mapped[str]
    date: Mapped[str] = mapped_column(TIMESTAMP)
    action: Mapped["Action"] = relationship("Action", back_populates="project_changes")
    component: Mapped["ProjectComponent"] = relationship("ProjectComponent", back_populates="project_changes")


playlist_song = Table('playlist_songs', db.Model.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('playlist_id', Integer, ForeignKey('playlist.id')),
                      Column('song_id', Integer, ForeignKey('songs.id')))


class Playlist(db.Model, SerializerMixin):
    __tablename__ = "playlist"
    serialize_rules = ('-songs.playlists',)
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    songs = relationship("Song", secondary=playlist_song, back_populates="playlists")


class Song(db.Model, SerializerMixin):
    __tablename__ = "songs"
    serialize_rules = ('-playlists.songs',)
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    playlists = relationship("Playlist", secondary=playlist_song, back_populates="songs")
