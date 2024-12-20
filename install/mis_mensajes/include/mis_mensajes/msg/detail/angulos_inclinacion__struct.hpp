// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from mis_mensajes:msg/AngulosInclinacion.idl
// generated code does not contain a copyright notice

#ifndef MIS_MENSAJES__MSG__DETAIL__ANGULOS_INCLINACION__STRUCT_HPP_
#define MIS_MENSAJES__MSG__DETAIL__ANGULOS_INCLINACION__STRUCT_HPP_

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
# define DEPRECATED__mis_mensajes__msg__AngulosInclinacion __attribute__((deprecated))
#else
# define DEPRECATED__mis_mensajes__msg__AngulosInclinacion __declspec(deprecated)
#endif

namespace mis_mensajes
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct AngulosInclinacion_
{
  using Type = AngulosInclinacion_<ContainerAllocator>;

  explicit AngulosInclinacion_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->roll = 0.0;
      this->pitch = 0.0;
      this->yaw = 0.0;
    }
  }

  explicit AngulosInclinacion_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->roll = 0.0;
      this->pitch = 0.0;
      this->yaw = 0.0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _roll_type =
    double;
  _roll_type roll;
  using _pitch_type =
    double;
  _pitch_type pitch;
  using _yaw_type =
    double;
  _yaw_type yaw;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__roll(
    const double & _arg)
  {
    this->roll = _arg;
    return *this;
  }
  Type & set__pitch(
    const double & _arg)
  {
    this->pitch = _arg;
    return *this;
  }
  Type & set__yaw(
    const double & _arg)
  {
    this->yaw = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator> *;
  using ConstRawPtr =
    const mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__mis_mensajes__msg__AngulosInclinacion
    std::shared_ptr<mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__mis_mensajes__msg__AngulosInclinacion
    std::shared_ptr<mis_mensajes::msg::AngulosInclinacion_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AngulosInclinacion_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->roll != other.roll) {
      return false;
    }
    if (this->pitch != other.pitch) {
      return false;
    }
    if (this->yaw != other.yaw) {
      return false;
    }
    return true;
  }
  bool operator!=(const AngulosInclinacion_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AngulosInclinacion_

// alias to use template instance with default allocator
using AngulosInclinacion =
  mis_mensajes::msg::AngulosInclinacion_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace mis_mensajes

#endif  // MIS_MENSAJES__MSG__DETAIL__ANGULOS_INCLINACION__STRUCT_HPP_
