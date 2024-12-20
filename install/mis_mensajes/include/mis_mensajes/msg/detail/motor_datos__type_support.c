// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from mis_mensajes:msg/MotorDatos.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "mis_mensajes/msg/detail/motor_datos__rosidl_typesupport_introspection_c.h"
#include "mis_mensajes/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "mis_mensajes/msg/detail/motor_datos__functions.h"
#include "mis_mensajes/msg/detail/motor_datos__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  mis_mensajes__msg__MotorDatos__init(message_memory);
}

void MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_fini_function(void * message_memory)
{
  mis_mensajes__msg__MotorDatos__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_message_member_array[3] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mis_mensajes__msg__MotorDatos, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rpm",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mis_mensajes__msg__MotorDatos, rpm),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "current",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mis_mensajes__msg__MotorDatos, current),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_message_members = {
  "mis_mensajes__msg",  // message namespace
  "MotorDatos",  // message name
  3,  // number of fields
  sizeof(mis_mensajes__msg__MotorDatos),
  MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_message_member_array,  // message members
  MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_init_function,  // function to initialize message memory (memory has to be allocated)
  MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_message_type_support_handle = {
  0,
  &MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mis_mensajes
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mis_mensajes, msg, MotorDatos)() {
  MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_message_type_support_handle.typesupport_identifier) {
    MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &MotorDatos__rosidl_typesupport_introspection_c__MotorDatos_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
