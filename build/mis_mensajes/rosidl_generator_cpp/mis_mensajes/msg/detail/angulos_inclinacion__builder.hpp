// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mis_mensajes:msg/AngulosInclinacion.idl
// generated code does not contain a copyright notice

#ifndef MIS_MENSAJES__MSG__DETAIL__ANGULOS_INCLINACION__BUILDER_HPP_
#define MIS_MENSAJES__MSG__DETAIL__ANGULOS_INCLINACION__BUILDER_HPP_

#include "mis_mensajes/msg/detail/angulos_inclinacion__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace mis_mensajes
{

namespace msg
{

namespace builder
{

class Init_AngulosInclinacion_yaw
{
public:
  explicit Init_AngulosInclinacion_yaw(::mis_mensajes::msg::AngulosInclinacion & msg)
  : msg_(msg)
  {}
  ::mis_mensajes::msg::AngulosInclinacion yaw(::mis_mensajes::msg::AngulosInclinacion::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mis_mensajes::msg::AngulosInclinacion msg_;
};

class Init_AngulosInclinacion_pitch
{
public:
  explicit Init_AngulosInclinacion_pitch(::mis_mensajes::msg::AngulosInclinacion & msg)
  : msg_(msg)
  {}
  Init_AngulosInclinacion_yaw pitch(::mis_mensajes::msg::AngulosInclinacion::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_AngulosInclinacion_yaw(msg_);
  }

private:
  ::mis_mensajes::msg::AngulosInclinacion msg_;
};

class Init_AngulosInclinacion_roll
{
public:
  explicit Init_AngulosInclinacion_roll(::mis_mensajes::msg::AngulosInclinacion & msg)
  : msg_(msg)
  {}
  Init_AngulosInclinacion_pitch roll(::mis_mensajes::msg::AngulosInclinacion::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_AngulosInclinacion_pitch(msg_);
  }

private:
  ::mis_mensajes::msg::AngulosInclinacion msg_;
};

class Init_AngulosInclinacion_header
{
public:
  Init_AngulosInclinacion_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AngulosInclinacion_roll header(::mis_mensajes::msg::AngulosInclinacion::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_AngulosInclinacion_roll(msg_);
  }

private:
  ::mis_mensajes::msg::AngulosInclinacion msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::mis_mensajes::msg::AngulosInclinacion>()
{
  return mis_mensajes::msg::builder::Init_AngulosInclinacion_header();
}

}  // namespace mis_mensajes

#endif  // MIS_MENSAJES__MSG__DETAIL__ANGULOS_INCLINACION__BUILDER_HPP_
