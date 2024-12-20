// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from mis_mensajes:msg/AngulosInclinacion.idl
// generated code does not contain a copyright notice
#include "mis_mensajes/msg/detail/angulos_inclinacion__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
mis_mensajes__msg__AngulosInclinacion__init(mis_mensajes__msg__AngulosInclinacion * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    mis_mensajes__msg__AngulosInclinacion__fini(msg);
    return false;
  }
  // roll
  // pitch
  // yaw
  return true;
}

void
mis_mensajes__msg__AngulosInclinacion__fini(mis_mensajes__msg__AngulosInclinacion * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // roll
  // pitch
  // yaw
}

bool
mis_mensajes__msg__AngulosInclinacion__are_equal(const mis_mensajes__msg__AngulosInclinacion * lhs, const mis_mensajes__msg__AngulosInclinacion * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // roll
  if (lhs->roll != rhs->roll) {
    return false;
  }
  // pitch
  if (lhs->pitch != rhs->pitch) {
    return false;
  }
  // yaw
  if (lhs->yaw != rhs->yaw) {
    return false;
  }
  return true;
}

bool
mis_mensajes__msg__AngulosInclinacion__copy(
  const mis_mensajes__msg__AngulosInclinacion * input,
  mis_mensajes__msg__AngulosInclinacion * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // roll
  output->roll = input->roll;
  // pitch
  output->pitch = input->pitch;
  // yaw
  output->yaw = input->yaw;
  return true;
}

mis_mensajes__msg__AngulosInclinacion *
mis_mensajes__msg__AngulosInclinacion__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mis_mensajes__msg__AngulosInclinacion * msg = (mis_mensajes__msg__AngulosInclinacion *)allocator.allocate(sizeof(mis_mensajes__msg__AngulosInclinacion), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(mis_mensajes__msg__AngulosInclinacion));
  bool success = mis_mensajes__msg__AngulosInclinacion__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
mis_mensajes__msg__AngulosInclinacion__destroy(mis_mensajes__msg__AngulosInclinacion * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    mis_mensajes__msg__AngulosInclinacion__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
mis_mensajes__msg__AngulosInclinacion__Sequence__init(mis_mensajes__msg__AngulosInclinacion__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mis_mensajes__msg__AngulosInclinacion * data = NULL;

  if (size) {
    data = (mis_mensajes__msg__AngulosInclinacion *)allocator.zero_allocate(size, sizeof(mis_mensajes__msg__AngulosInclinacion), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = mis_mensajes__msg__AngulosInclinacion__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        mis_mensajes__msg__AngulosInclinacion__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
mis_mensajes__msg__AngulosInclinacion__Sequence__fini(mis_mensajes__msg__AngulosInclinacion__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      mis_mensajes__msg__AngulosInclinacion__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

mis_mensajes__msg__AngulosInclinacion__Sequence *
mis_mensajes__msg__AngulosInclinacion__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mis_mensajes__msg__AngulosInclinacion__Sequence * array = (mis_mensajes__msg__AngulosInclinacion__Sequence *)allocator.allocate(sizeof(mis_mensajes__msg__AngulosInclinacion__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = mis_mensajes__msg__AngulosInclinacion__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
mis_mensajes__msg__AngulosInclinacion__Sequence__destroy(mis_mensajes__msg__AngulosInclinacion__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    mis_mensajes__msg__AngulosInclinacion__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
mis_mensajes__msg__AngulosInclinacion__Sequence__are_equal(const mis_mensajes__msg__AngulosInclinacion__Sequence * lhs, const mis_mensajes__msg__AngulosInclinacion__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!mis_mensajes__msg__AngulosInclinacion__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
mis_mensajes__msg__AngulosInclinacion__Sequence__copy(
  const mis_mensajes__msg__AngulosInclinacion__Sequence * input,
  mis_mensajes__msg__AngulosInclinacion__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(mis_mensajes__msg__AngulosInclinacion);
    mis_mensajes__msg__AngulosInclinacion * data =
      (mis_mensajes__msg__AngulosInclinacion *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!mis_mensajes__msg__AngulosInclinacion__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          mis_mensajes__msg__AngulosInclinacion__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!mis_mensajes__msg__AngulosInclinacion__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
