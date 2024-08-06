        import numpy as np

        def detect_outliers(data):
            threshold = 3
            mean = np.mean(data)
            std = np.std(data)
            
            outliers = []
            for i in data:
                z_score = (i - mean)/std
                if np.abs(z_score) > threshold:
                    outliers.append(i)
            return outliers

        data = [10, 12, 14, 15, 18, 100, 101]  # Example data
        outliers = detect_outliers(data)
        print("Outliers:", outliers)
        