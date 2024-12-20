// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from mis_mensajes:msg/MotorDatos.idl
// generated code does not contain a copyright notice

#ifndef MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__TRAITS_HPP_
#define MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__TRAITS_HPP_

#include "mis_mensajes/msg/detail/motor_datos__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<mis_mensajes::msg::MotorDatos>()
{
  return "mis_mensajes::msg::MotorDatos";
}

template<>
inline const char * name<mis_mensajes::msg::MotorDatos>()
{
  return "mis_mensajes/msg/MotorDatos";
}

template<>
struct has_fixed_size<mis_mensajes::msg::MotorDatos>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<mis_mensajes::msg::MotorDatos>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<mis_mensajes::msg::MotorDatos>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__TRAITS_HPP_
