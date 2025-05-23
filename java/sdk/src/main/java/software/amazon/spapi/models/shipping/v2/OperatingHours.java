/*
 * Amazon Shipping API
 * The Amazon Shipping API is designed to support outbound shipping use cases both for orders originating on Amazon-owned marketplaces as well as external channels/marketplaces. With these APIs, you can request shipping rates, create shipments, cancel shipments, and track shipments.
 *
 * OpenAPI spec version: v2
 * Contact: swa-api-core@amazon.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package software.amazon.spapi.models.shipping.v2;

import com.google.gson.annotations.SerializedName;
import io.swagger.v3.oas.annotations.media.Schema;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/** The hours in which the access point shall remain operational */
@Schema(description = "The hours in which the access point shall remain operational")
public class OperatingHours {
    @SerializedName("closingTime")
    private TimeOfDay closingTime = null;

    @SerializedName("openingTime")
    private TimeOfDay openingTime = null;

    @SerializedName("midDayClosures")
    private List<TimeOfDay> midDayClosures = null;

    public OperatingHours closingTime(TimeOfDay closingTime) {
        this.closingTime = closingTime;
        return this;
    }

    /**
     * Get closingTime
     *
     * @return closingTime
     */
    @Schema(description = "")
    public TimeOfDay getClosingTime() {
        return closingTime;
    }

    public void setClosingTime(TimeOfDay closingTime) {
        this.closingTime = closingTime;
    }

    public OperatingHours openingTime(TimeOfDay openingTime) {
        this.openingTime = openingTime;
        return this;
    }

    /**
     * Get openingTime
     *
     * @return openingTime
     */
    @Schema(description = "")
    public TimeOfDay getOpeningTime() {
        return openingTime;
    }

    public void setOpeningTime(TimeOfDay openingTime) {
        this.openingTime = openingTime;
    }

    public OperatingHours midDayClosures(List<TimeOfDay> midDayClosures) {
        this.midDayClosures = midDayClosures;
        return this;
    }

    public OperatingHours addMidDayClosuresItem(TimeOfDay midDayClosuresItem) {
        if (this.midDayClosures == null) {
            this.midDayClosures = new ArrayList<TimeOfDay>();
        }
        this.midDayClosures.add(midDayClosuresItem);
        return this;
    }

    /**
     * midDayClosures operating hours array
     *
     * @return midDayClosures
     */
    @Schema(description = "midDayClosures operating hours array")
    public List<TimeOfDay> getMidDayClosures() {
        return midDayClosures;
    }

    public void setMidDayClosures(List<TimeOfDay> midDayClosures) {
        this.midDayClosures = midDayClosures;
    }

    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        OperatingHours operatingHours = (OperatingHours) o;
        return Objects.equals(this.closingTime, operatingHours.closingTime)
                && Objects.equals(this.openingTime, operatingHours.openingTime)
                && Objects.equals(this.midDayClosures, operatingHours.midDayClosures);
    }

    @Override
    public int hashCode() {
        return Objects.hash(closingTime, openingTime, midDayClosures);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class OperatingHours {\n");

        sb.append("    closingTime: ").append(toIndentedString(closingTime)).append("\n");
        sb.append("    openingTime: ").append(toIndentedString(openingTime)).append("\n");
        sb.append("    midDayClosures: ")
                .append(toIndentedString(midDayClosures))
                .append("\n");
        sb.append("}");
        return sb.toString();
    }

    /** Convert the given object to string with each line indented by 4 spaces (except the first line). */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }
}
