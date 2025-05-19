import uuid
from datetime import datetime, UTC

from sqlalchemy import (
    Column, String, Boolean, Integer, Float, ForeignKey, DateTime, Text
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Arduino(Base):
    __tablename__ = 'arduinos'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    is_environment_tracker = Column(Boolean, default=False)
    serial_port = Column(String, nullable=False)
    soil_temp_pin = Column(Integer)
    soil_moisture_pin = Column(Integer)
    pump_control_pin = Column(Integer)

    # Reverse relationship to Plant
    plant = relationship("Plant", back_populates="arduino", uselist=False)

    # Relationships to logs
    light_logs = relationship("LightLog", back_populates="arduino")
    air_quality_logs = relationship("AirQualityLog", back_populates="arduino")
    ambient_temp_logs = relationship("AmbientTempLog", back_populates="arduino")


class Plant(Base):
    __tablename__ = 'plants'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    enabled = Column(Boolean, default=True)
    plant_name = Column(String, nullable=False)
    plant_type = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    arduino_id = Column(UUID(as_uuid=True), ForeignKey('arduinos.id'))

    # Relationship to Arduino
    arduino = relationship("Arduino", back_populates="plant")

    # Relationships to logs
    soil_temp_logs = relationship("SoilTemperatureLog", back_populates="plant")
    soil_moisture_logs = relationship("SoilMoistureLog", back_populates="plant")
    watering_logs = relationship("WateringLog", back_populates="plant")


# Logs per plant
class SoilTemperatureLog(Base):
    __tablename__ = 'soil_temperature_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    plant_id = Column(UUID(as_uuid=True), ForeignKey('plants.id'), nullable=False)
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    value = Column(Float, nullable=False)

    plant = relationship("Plant", back_populates="soil_temp_logs")


class SoilMoistureLog(Base):
    __tablename__ = 'soil_moisture_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    plant_id = Column(UUID(as_uuid=True), ForeignKey('plants.id'), nullable=False)
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    value = Column(Float, nullable=False)

    plant = relationship("Plant", back_populates="soil_moisture_logs")


class WateringLog(Base):
    __tablename__ = 'watering_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    plant_id = Column(UUID(as_uuid=True), ForeignKey('plants.id'), nullable=False)
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    duration = Column(Float, nullable=False)
    volume = Column(Float, nullable=True)

    plant = relationship("Plant", back_populates="watering_logs")


# Logs per arduino (environmental)
class LightLog(Base):
    __tablename__ = 'light_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    arduino_id = Column(UUID(as_uuid=True), ForeignKey('arduinos.id'), nullable=False)
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    value = Column(Float, nullable=False)

    arduino = relationship("Arduino", back_populates="light_logs")


class AirQualityLog(Base):
    __tablename__ = 'air_quality_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    arduino_id = Column(UUID(as_uuid=True), ForeignKey('arduinos.id'), nullable=False)
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    value = Column(Float, nullable=False)

    arduino = relationship("Arduino", back_populates="air_quality_logs")


class AmbientTempLog(Base):
    __tablename__ = 'ambient_temp_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    arduino_id = Column(UUID(as_uuid=True), ForeignKey('arduinos.id'), nullable=False)
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    value = Column(Float, nullable=False)

    arduino = relationship("Arduino", back_populates="ambient_temp_logs")
