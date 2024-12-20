// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from mis_mensajes:msg/AngulosInclinacion.idl
// generated code does not contain a copyright notice

#ifndef MIS_MENSAJES__MSG__DETAIL__ANGULOS_INCLINACION__STRUCT_H_
#define MIS_MENSAJES__MSG__DETAIL__ANGULOS_INCLINACION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

// Struct defined in msg/AngulosInclinacion in the package mis_mensajes.
typedef struct mis_mensajes__msg__AngulosInclinacion
{
  std_msgs__msg__Header header;
  double roll;
  double pitch;
  double yaw;
} mis_mensajes__msg__AngulosInclinacion;

// Struct for a sequence of mis_mensajes__msg__AngulosInclinacion.
typedef struct mis_mensajes__msg__AngulosInclinacion__Sequence
{
  mis_mensajes__msg__AngulosInclinacion * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} mis_mensajes__msg__AngulosInclinacion__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MIS_MENSAJES__MSG__DETAIL__ANGULOS_INCLINACION__STRUCT_H_
