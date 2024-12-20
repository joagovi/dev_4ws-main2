// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from mis_mensajes:msg/MotorDatos.idl
// generated code does not contain a copyright notice

#ifndef MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__FUNCTIONS_H_
#define MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "mis_mensajes/msg/rosidl_generator_c__visibility_control.h"

#include "mis_mensajes/msg/detail/motor_datos__struct.h"

/// Initialize msg/MotorDatos message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * mis_mensajes__msg__MotorDatos
 * )) before or use
 * mis_mensajes__msg__MotorDatos__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
bool
mis_mensajes__msg__MotorDatos__init(mis_mensajes__msg__MotorDatos * msg);

/// Finalize msg/MotorDatos message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
void
mis_mensajes__msg__MotorDatos__fini(mis_mensajes__msg__MotorDatos * msg);

/// Create msg/MotorDatos message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * mis_mensajes__msg__MotorDatos__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
mis_mensajes__msg__MotorDatos *
mis_mensajes__msg__MotorDatos__create();

/// Destroy msg/MotorDatos message.
/**
 * It calls
 * mis_mensajes__msg__MotorDatos__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
void
mis_mensajes__msg__MotorDatos__destroy(mis_mensajes__msg__MotorDatos * msg);

/// Check for msg/MotorDatos message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
bool
mis_mensajes__msg__MotorDatos__are_equal(const mis_mensajes__msg__MotorDatos * lhs, const mis_mensajes__msg__MotorDatos * rhs);

/// Copy a msg/MotorDatos message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
bool
mis_mensajes__msg__MotorDatos__copy(
  const mis_mensajes__msg__MotorDatos * input,
  mis_mensajes__msg__MotorDatos * output);

/// Initialize array of msg/MotorDatos messages.
/**
 * It allocates the memory for the number of elements and calls
 * mis_mensajes__msg__MotorDatos__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
bool
mis_mensajes__msg__MotorDatos__Sequence__init(mis_mensajes__msg__MotorDatos__Sequence * array, size_t size);

/// Finalize array of msg/MotorDatos messages.
/**
 * It calls
 * mis_mensajes__msg__MotorDatos__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
void
mis_mensajes__msg__MotorDatos__Sequence__fini(mis_mensajes__msg__MotorDatos__Sequence * array);

/// Create array of msg/MotorDatos messages.
/**
 * It allocates the memory for the array and calls
 * mis_mensajes__msg__MotorDatos__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
mis_mensajes__msg__MotorDatos__Sequence *
mis_mensajes__msg__MotorDatos__Sequence__create(size_t size);

/// Destroy array of msg/MotorDatos messages.
/**
 * It calls
 * mis_mensajes__msg__MotorDatos__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
void
mis_mensajes__msg__MotorDatos__Sequence__destroy(mis_mensajes__msg__MotorDatos__Sequence * array);

/// Check for msg/MotorDatos message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
bool
mis_mensajes__msg__MotorDatos__Sequence__are_equal(const mis_mensajes__msg__MotorDatos__Sequence * lhs, const mis_mensajes__msg__MotorDatos__Sequence * rhs);

/// Copy an array of msg/MotorDatos messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_mis_mensajes
bool
mis_mensajes__msg__MotorDatos__Sequence__copy(
  const mis_mensajes__msg__MotorDatos__Sequence * input,
  mis_mensajes__msg__MotorDatos__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__FUNCTIONS_H_
