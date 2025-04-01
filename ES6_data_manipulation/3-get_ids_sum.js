export default function getStudentIdsSum(students) {
  return students.reduce((value, student) => value + student.id, 0);
}
