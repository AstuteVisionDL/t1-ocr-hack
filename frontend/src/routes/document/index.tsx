import { FC } from "react";

import MainLayout from "../../layouts/MainLayout";
import DocumentUploader from "./components/DocumentUploader.tsx";

const Document: FC = () => {
  return (
    <MainLayout>
      <DocumentUploader />
    </MainLayout>
  );
};

export default Document;
