class interpolation:

    def linear_interpolation(self, top_val, bottom_val, weight):
        """Computes the linear interpolation value at some iD location x between two 1D points (Pt1 and Pt2).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes two 1D points Pt1 and Pt2, and their intensitites I(Pt1), I(Pt2).
        return the interpolated intensity value (I(x)) at location x """

        return top_val * (1 - weight) + bottom_val * weight

    def bilinear_interpolation(self, top_left, top_right, bottom_left, bottom_right, x_weight, y_weight):
        """Computes the bilinear interpolation value at some 2D location x between four 2D points (Pt1, Pt2, Pt3, and Pt4).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes four 2D points Pt1, Pt2, Pt3, and Pt4, and their intensitites I(Pt1), I(Pt2), I(Pt3), and I(Pt4).
        return the interpolated intensity value (I(x)) at location x """

        top_interp = self.linear_interpolation(top_left, top_right, x_weight)
        bottom_interp = self.linear_interpolation(bottom_left, bottom_right, x_weight)
        final_value = self.linear_interpolation(top_interp, bottom_interp, y_weight)
        
        return final_value
