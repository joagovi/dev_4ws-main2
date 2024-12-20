// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from mis_mensajes:msg/AngulosInclinacion.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "mis_mensajes/msg/detail/angulos_inclinacion__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace mis_mensajes
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void AngulosInclinacion_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) mis_mensajes::msg::AngulosInclinacion(_init);
}

void AngulosInclinacion_fini_function(void * message_memory)
{
  auto typed_message = static_cast<mis_mensajes::msg::AngulosInclinacion *>(message_memory);
  typed_message->~AngulosInclinacion();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember AngulosInclinacion_message_member_array[4] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mis_mensajes::msg::AngulosInclinacion, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "roll",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mis_mensajes::msg::AngulosInclinacion, roll),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "pitch",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mis_mensajes::msg::AngulosInclinacion, pitch),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "yaw",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mis_mensajes::msg::AngulosInclinacion, yaw),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers AngulosInclinacion_message_members = {
  "mis_mensajes::msg",  // message namespace
  "AngulosInclinacion",  // message name
  4,  // number of fields
  sizeof(mis_mensajes::msg::AngulosInclinacion),
  AngulosInclinacion_message_member_array,  // message members
  AngulosInclinacion_init_function,  // function to initialize message memory (memory has to be allocated)
  AngulosInclinacion_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t AngulosInclinacion_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &AngulosInclinacion_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace mis_mensajes


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<mis_mensajes::msg::AngulosInclinacion>()
{
  return &::mis_mensajes::msg::rosidl_typesupport_introspection_cpp::AngulosInclinacion_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, mis_mensajes, msg, AngulosInclinacion)() {
  return &::mis_mensajes::msg::rosidl_typesupport_introspection_cpp::AngulosInclinacion_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
