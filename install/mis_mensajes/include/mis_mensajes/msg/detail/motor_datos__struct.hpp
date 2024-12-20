// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from mis_mensajes:msg/MotorDatos.idl
// generated code does not contain a copyright notice

#ifndef MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__STRUCT_HPP_
#define MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__mis_mensajes__msg__MotorDatos __attribute__((deprecated))
#else
# define DEPRECATED__mis_mensajes__msg__MotorDatos __declspec(deprecated)
#endif

namespace mis_mensajes
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MotorDatos_
{
  using Type = MotorDatos_<ContainerAllocator>;

  explicit MotorDatos_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->rpm = 0l;
      this->current = 0.0f;
    }
  }

  explicit MotorDatos_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->rpm = 0l;
      this->current = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _rpm_type =
    int32_t;
  _rpm_type rpm;
  using _current_type =
    float;
  _current_type current;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__rpm(
    const int32_t & _arg)
  {
    this->rpm = _arg;
    return *this;
  }
  Type & set__current(
    const float & _arg)
  {
    this->current = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    mis_mensajes::msg::MotorDatos_<ContainerAllocator> *;
  using ConstRawPtr =
    const mis_mensajes::msg::MotorDatos_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<mis_mensajes::msg::MotorDatos_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<mis_mensajes::msg::MotorDatos_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      mis_mensajes::msg::MotorDatos_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<mis_mensajes::msg::MotorDatos_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      mis_mensajes::msg::MotorDatos_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<mis_mensajes::msg::MotorDatos_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<mis_mensajes::msg::MotorDatos_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<mis_mensajes::msg::MotorDatos_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__mis_mensajes__msg__MotorDatos
    std::shared_ptr<mis_mensajes::msg::MotorDatos_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__mis_mensajes__msg__MotorDatos
    std::shared_ptr<mis_mensajes::msg::MotorDatos_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MotorDatos_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->rpm != other.rpm) {
      return false;
    }
    if (this->current != other.current) {
      return false;
    }
    return true;
  }
  bool operator!=(const MotorDatos_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MotorDatos_

// alias to use template instance with default allocator
using MotorDatos =
  mis_mensajes::msg::MotorDatos_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace mis_mensajes

#endif  // MIS_MENSAJES__MSG__DETAIL__MOTOR_DATOS__STRUCT_HPP_
