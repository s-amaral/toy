# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main/exchange_simulator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dmain/exchange_simulator.proto\x12\x08\x65xchange\"e\n\rStreamRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08\x63lientId\x12\x18\n\x07symbols\x18\x03 \x03(\tR\x07symbols\"\xde\x01\n\x12\x45xchangeDataUpdate\x12\x1c\n\ttimestamp\x18\x01 \x01(\x03R\ttimestamp\x12\x35\n\x0bmarket_data\x18\x02 \x03(\x0b\x32\x14.exchange.MarketDataR\nmarketData\x12:\n\rorder_updates\x18\x03 \x03(\x0b\x32\x15.exchange.OrderUpdateR\x0corderUpdates\x12\x37\n\tportfolio\x18\x04 \x01(\x0b\x32\x19.exchange.PortfolioStatusR\tportfolio\"\xba\x01\n\nMarketData\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x10\n\x03\x62id\x18\x02 \x01(\x01R\x03\x62id\x12\x10\n\x03\x61sk\x18\x03 \x01(\x01R\x03\x61sk\x12\x19\n\x08\x62id_size\x18\x04 \x01(\x05R\x07\x62idSize\x12\x19\n\x08\x61sk_size\x18\x05 \x01(\x05R\x07\x61skSize\x12\x1d\n\nlast_price\x18\x06 \x01(\x01R\tlastPrice\x12\x1b\n\tlast_size\x18\x07 \x01(\x05R\x08lastSize\"\xa6\x01\n\x0bOrderUpdate\x12\x19\n\x08order_id\x18\x01 \x01(\tR\x07orderId\x12\x16\n\x06symbol\x18\x02 \x01(\tR\x06symbol\x12\x16\n\x06status\x18\x03 \x01(\tR\x06status\x12\'\n\x0f\x66illed_quantity\x18\x04 \x01(\x05R\x0e\x66illedQuantity\x12#\n\raverage_price\x18\x05 \x01(\x01R\x0c\x61veragePrice\"\x87\x01\n\x0fPortfolioStatus\x12\x30\n\tpositions\x18\x01 \x03(\x0b\x32\x12.exchange.PositionR\tpositions\x12!\n\x0c\x63\x61sh_balance\x18\x02 \x01(\x01R\x0b\x63\x61shBalance\x12\x1f\n\x0btotal_value\x18\x03 \x01(\x01R\ntotalValue\"\x84\x01\n\x08Position\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1a\n\x08quantity\x18\x02 \x01(\x05R\x08quantity\x12!\n\x0c\x61verage_cost\x18\x03 \x01(\x01R\x0b\x61verageCost\x12!\n\x0cmarket_value\x18\x04 \x01(\x01R\x0bmarketValue\"y\n\x10HeartbeatRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08\x63lientId\x12)\n\x10\x63lient_timestamp\x18\x03 \x01(\x03R\x0f\x63lientTimestamp\"X\n\x11HeartbeatResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12)\n\x10server_timestamp\x18\x02 \x01(\x03R\x0fserverTimestamp2\xa8\x01\n\x11\x45xchangeSimulator\x12M\n\x12StreamExchangeData\x12\x17.exchange.StreamRequest\x1a\x1c.exchange.ExchangeDataUpdate0\x01\x12\x44\n\tHeartbeat\x12\x1a.exchange.HeartbeatRequest\x1a\x1b.exchange.HeartbeatResponseBf\n\x0c\x63om.exchangeB\x16\x45xchangeSimulatorProtoP\x01\xa2\x02\x03\x45XX\xaa\x02\x08\x45xchange\xca\x02\x08\x45xchange\xe2\x02\x14\x45xchange\\GPBMetadata\xea\x02\x08\x45xchangeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'main.exchange_simulator_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\014com.exchangeB\026ExchangeSimulatorProtoP\001\242\002\003EXX\252\002\010Exchange\312\002\010Exchange\342\002\024Exchange\\GPBMetadata\352\002\010Exchange'
  _STREAMREQUEST._serialized_start=43
  _STREAMREQUEST._serialized_end=144
  _EXCHANGEDATAUPDATE._serialized_start=147
  _EXCHANGEDATAUPDATE._serialized_end=369
  _MARKETDATA._serialized_start=372
  _MARKETDATA._serialized_end=558
  _ORDERUPDATE._serialized_start=561
  _ORDERUPDATE._serialized_end=727
  _PORTFOLIOSTATUS._serialized_start=730
  _PORTFOLIOSTATUS._serialized_end=865
  _POSITION._serialized_start=868
  _POSITION._serialized_end=1000
  _HEARTBEATREQUEST._serialized_start=1002
  _HEARTBEATREQUEST._serialized_end=1123
  _HEARTBEATRESPONSE._serialized_start=1125
  _HEARTBEATRESPONSE._serialized_end=1213
  _EXCHANGESIMULATOR._serialized_start=1216
  _EXCHANGESIMULATOR._serialized_end=1384
# @@protoc_insertion_point(module_scope)
