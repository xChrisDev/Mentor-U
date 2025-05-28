import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

const createStudentSolution = async (problemId, studentId, mentorieId, code, comments, result) => {
  try {
    const response = await axios.post(`${BASE_URL}/student-solutions/`, {
      problem_id: problemId,
      student_id: studentId,
      mentorie_id: mentorieId,
      code: code,
      comments: comments || "",
      result: result
    });
    return response.data;
  } catch (error) {
    console.error('Error creating solution:', error);
    throw error;
  }
};

const getStudentSolutionDetails = async (solutionId) => {
  try {
    const response = await axios.get(`${BASE_URL}/student-solutions/${solutionId}`);
    return response.data;
  } catch (error) {
    console.error('Error getting solution:', error);
    throw error;
  }
};

const getAllStudentSolutions = async (filters = {}) => {
  try {
    let url = `${BASE_URL}/student-solutions/`;
    const params = new URLSearchParams();
    
    if (filters.studentId) params.append('student_id', filters.studentId);
    if (filters.problemId) params.append('problem_id', filters.problemId);
    if (filters.mentorieId) params.append('mentorie_id', filters.mentorieId);
    if (filters.result) params.append('result', filters.result);
    
    if (params.toString()) {
      url += `?${params.toString()}`;
    }
    
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error('Error getting all solutions:', error);
    throw error;
  }
};

const updateStudentSolution = async (solutionId, updates) => {
  try {
    const response = await axios.put(`${BASE_URL}/student-solutions/${solutionId}`, updates);
    return response.data;
  } catch (error) {
    console.error('Error updating solution:', error);
    throw error;
  }
};

const deleteStudentSolution = async (solutionId) => {
  try {
    const response = await axios.delete(`${BASE_URL}/student-solutions/${solutionId}`);
    return response.status === 204;
  } catch (error) {
    console.error('Error deleting solution:', error);
    throw error;
  }
};

const getStudentSolutionsByMentorie = async (studentId, mentorieId) => {
  try {
    const response = await axios.get(`${BASE_URL}/student-solutions/student/${studentId}/mentorie/${mentorieId}`);
    return response.data;
  } catch (error) {
    console.error('Error getting solutions by mentorie:', error);
    throw error;
  }
};