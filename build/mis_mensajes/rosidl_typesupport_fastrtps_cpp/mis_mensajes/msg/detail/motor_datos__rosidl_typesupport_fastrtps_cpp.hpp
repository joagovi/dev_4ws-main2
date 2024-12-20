// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from mis_mensajes:msg/MotorDatos.idl
// generated code does not contain a copyright notice

#ifndef MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "mis_mensajes/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "mis_mensajes/msg/detail/motor_datos__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace mis_mensajes
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mis_mensajes
cdr_serialize(
  const mis_mensajes::msg::MotorDatos & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mis_mensajes
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  mis_mensajes::msg::MotorDatos & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mis_mensajes
get_serialized_size(
  const mis_mensajes::msg::MotorDatos & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mis_mensajes
max_serialized_size_MotorDatos(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace mis_mensajes

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mis_mensajes
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, mis_mensajes, msg, MotorDatos)();

#ifdef __cplusplus
}
#endif

#endif  // MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
