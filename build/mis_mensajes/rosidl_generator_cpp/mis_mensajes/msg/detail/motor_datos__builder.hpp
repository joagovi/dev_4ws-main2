// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mis_mensajes:msg/MotorDatos.idl
// generated code does not contain a copyright notice

#ifndef MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__BUILDER_HPP_
#define MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__BUILDER_HPP_

#include "mis_mensajes/msg/detail/motor_datos__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace mis_mensajes
{

namespace msg
{

namespace builder
{

class Init_MotorDatos_current
{
public:
  explicit Init_MotorDatos_current(::mis_mensajes::msg::MotorDatos & msg)
  : msg_(msg)
  {}
  ::mis_mensajes::msg::MotorDatos current(::mis_mensajes::msg::MotorDatos::_current_type arg)
  {
    msg_.current = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mis_mensajes::msg::MotorDatos msg_;
};

class Init_MotorDatos_rpm
{
public:
  explicit Init_MotorDatos_rpm(::mis_mensajes::msg::MotorDatos & msg)
  : msg_(msg)
  {}
  Init_MotorDatos_current rpm(::mis_mensajes::msg::MotorDatos::_rpm_type arg)
  {
    msg_.rpm = std::move(arg);
    return Init_MotorDatos_current(msg_);
  }

private:
  ::mis_mensajes::msg::MotorDatos msg_;
};

class Init_MotorDatos_header
{
public:
  Init_MotorDatos_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MotorDatos_rpm header(::mis_mensajes::msg::MotorDatos::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_MotorDatos_rpm(msg_);
  }

private:
  ::mis_mensajes::msg::MotorDatos msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::mis_mensajes::msg::MotorDatos>()
{
  return mis_mensajes::msg::builder::Init_MotorDatos_header();
}

}  // namespace mis_mensajes

#endif  // MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__BUILDER_HPP_
